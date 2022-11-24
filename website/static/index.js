//take note id as an argument 
// send it to delete-note end point as a post request
// redirect the page to home page


function deleteNote(noteId){
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId:noteId})
    }).then((_res) => {
        window.location.href = "/";
    })
}