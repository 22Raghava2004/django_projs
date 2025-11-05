from django.shortcuts import render
import qrcode
import os

def hello(request):
    return render(request, 'hello.html')

def qecode(request):
    if request.method == "POST":
        # Get data from form
        data = request.POST.get('data')
        file = request.POST.get('file')

        if data and file:
            # Ensure 'static' folder exists
            if not os.path.exists("static"):
                os.makedirs("static")

            # Create QR code
            qr = qrcode.QRCode(box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)

            # Generate QR image
            image = qr.make_image(fill_color="black", back_color="white")

            # Save QR image in static folder
            image_path = f"static/{file}.png"
            image.save(image_path)

            # Render template with image
            return render(request, 'hello.html', {'image': image_path})

    # For GET request
    return render(request, 'hello.html')
