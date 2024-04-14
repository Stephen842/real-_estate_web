document.getElementById('prev').addEventListener('click', function() {
    document.querySelector('.slides').style.transform = 'translateX(-100%)';
});

document.getElementById('next').addEventListener('click', function() {
    document.querySelector('.slides').style.transform = 'translateX(100%)';
});

