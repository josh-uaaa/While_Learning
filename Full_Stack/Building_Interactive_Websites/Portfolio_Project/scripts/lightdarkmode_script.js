const lightdarkButton = document.getElementById('lightdark');
const lightdarkImg = document.getElementById('lightdark-img');
const techstackLogos = document.querySelectorAll('.tech-logo');
const socialsLogos = document.querySelectorAll('.social-logo');

let lightMode = true;
function changeMode() {
    if (lightMode) {
        document.body.style.backgroundColor = '#041C32';
        document.body.style.color = 'white';
        lightdarkImg.src = 'imgs/light_mode.png';
        lightdarkButton.style.borderColor = 'white';
        lightdarkButton.style.boxShadow = 'rgba(255, 255, 255, 0.4) 0 2px 4px, rgba(255, 255, 255, 0.3) 0 7px 13px -3px';
        socialsLogos.forEach((logo) => {
            const logoID = logo.id;
            logo.src = `imgs/${logoID}_dark.png`;
        });
        techstackLogos.forEach((logo) => {
            const logoID = logo.id;
            logo.src = `imgs/${logoID}_dark.png`;
        });
    } else {
        document.body.style.backgroundColor = '#F5F2E7';
        document.body.style.color = 'black'
        lightdarkImg.src = 'imgs/dark_mode.png';
        lightdarkButton.style.borderColor = 'black';
        lightdarkButton.style.boxShadow = 'rgba(45, 35, 66, 0.4) 0 2px 4px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px';
        socialsLogos.forEach((logo) => {
            const logoID = logo.id;
            logo.src = `imgs/${logoID}_light.png`;
        });
        techstackLogos.forEach((logo) => {
            const logoID = logo.id;
            logo.src = `imgs/${logoID}_light.png`;
        });
    }
    lightMode = !lightMode;
}

lightdarkButton.addEventListener('click', changeMode);