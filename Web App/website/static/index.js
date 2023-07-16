function deleteNote(noteID){
    // we are reloading the note with the get post request so that it gets deleted
    fetch('/delete-note', {
        method:'POST',
        body:JSON.stringify({ noteID: noteID})
    }).then((_res)=> {
        window.location.href='/';
    });
}