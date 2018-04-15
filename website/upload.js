fileUpload = document.getElementById("file-upload");
faceSearch = document.getElementById("face-search");
submitBtn = document.getElementById("submit-btn");

faceSearch.onclick = function(){
  fileUpload.click();
}

fileUpload.onchange = function(){
  submitBtn.click();
}
