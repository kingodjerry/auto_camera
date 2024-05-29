function addImagesToSlider(photosList) {
    const imageSlider = document.getElementById("image-slider");
    photosList.forEach(photo => {
        // Assuming the server returns Base64 encoded image data
        const img = document.createElement("img");
        img.src = `data:image/jpeg;base64, ${photo.img}`; // Adjust mimetype as needed
        img.alt = photo.filename;
        imageSlider.appendChild(img);
    });
}

async function fetchPhotos() {
    try {
        const response = await fetch("/photos");
        if (!response.ok) {
            throw new Error("서버로부터 이미지를 가져오는 데 실패했습니다.");
        }
        const photosList = await response.json();
        addImagesToSlider(photosList);
    } catch (error) {
        console.error("오류:", error);
    }
}

// 페이지 로드 시 이미지를 가져옴
window.addEventListener("load", fetchPhotos);

async function resetPhotos() {
    try {
        const response = await fetch("/reset_photos", {
            method: "POST"
        });
        if (!response.ok) {
            throw new Error("서버와의 통신 중 오류가 발생했습니다.");
        }
        console.log("모든 사진이 성공적으로 삭제되었습니다.");
    } catch (error) {
        console.error("오류:", error);
    }
}

// 페이지 로드 시 버튼에 이벤트 리스너 추가
window.addEventListener("load", function() {
    const resetButton = document.getElementById("reset-button");
    resetButton.addEventListener("click", resetPhotos);
});