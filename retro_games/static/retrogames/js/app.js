function openModal(url) {
    document.getElementById("modalImage").src = url;
    document.getElementById("imageModal").style.display = "block";
}
function closeModal() {
    document.getElementById("imageModal").style.display = "none";
}