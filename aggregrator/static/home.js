const readmores = document.querySelectorAll('.readmore');

for (const readmore of readmores) {
    readmore.addEventListener('click', (e) => {        
        const bodytext = e.target.previousElementSibling;        
        bodytext.classList.toggle("text-truncate")
        if (e.target.innerText === "Read More") {
            e.target.innerText = "Read Less"            
        } else {
            e.target.innerText = "Read More"
        }
        
    });
}

