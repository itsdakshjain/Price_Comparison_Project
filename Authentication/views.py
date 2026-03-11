from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# 1. This handles the Home/Dashboard page
def home(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_query')
        product_image = request.FILES.get('product_image')
        
        print(f"User searched for: {product_name}")
        print(f"User uploaded image: {product_image}")
        
        return render(request, 'home.html', {
            'searched': product_name,
            'image_name': product_image
        })
        
    return render(request, 'home.html')

# 2. This handles the Registration (Sign Up) page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            
            # --- THE FIX: Specify the backend ---
            login(request, user, backend='django.contrib.auth.backends.ModelBackend') 
            
            return redirect('home') 
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})