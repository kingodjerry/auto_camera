document.addEventListener('DOMContentLoaded', function() {
    fetch('/photos')
        .then(response => response.json())
        .then(data => {
            const imageSlider = document.getElementById('image-slider');
            data.forEach(photo => {
                const img = document.createElement('img');
                img.src = photo.filepath;
                imageSlider.appendChild(img);
            });
        })
        .catch(error => console.error('Error fetching photos:', error));
});