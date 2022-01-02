const submitBtn = document.querySelector('#submitBtn');
submitBtn.addEventListener('click', (e) => {    
    const message = document.querySelector('#message');
    const progressBar = document.querySelector('.progress');
    const theBar = document.querySelector('.progress-bar');    
    message.classList.toggle('d-none');
    progressBar.classList.toggle('d-none');
    theBar.classList.toggle("d-none");
    e.target.classList.toggle("d-none");    
    setInterval( () => {        
        theBar.style.width = parseInt((theBar.style.width).replace('%', '')) + 5 + "%" ;
    }, 1000);
    if (theBar.style.width === "100%") {
        clearInterval(barInterval);
    }
    
});

