const imageHolder = document.getElementById('image-holder');
const inputImage = document.getElementById('input-image');
console.log('js connected')
inputImage.addEventListener('change',()=>{
    if(inputImage.files && inputImage.files[0])
    {
        // reader filereader object to read the files
        const reader = new FileReader();
        
        reader.onload = function(e) {
            // Set the src attribute of the image tag to the data URL of the selected image
            imageHolder.src = e.target.result;
            console.log('image changed')
        };

        // Read the selected file as a data URL
        reader.readAsDataURL(inputImage.files[0]);
    }
})