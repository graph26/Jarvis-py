// Сохраняем оригинальные размеры
originalWidth = 556;
originalHeight = 703;

if (originalHeight !== window.innerHeight || originalWidth !== window.innerWidth){
    console.log('User did wants transform size window')
    // Блокируем масштабирование
    document.querySelector('meta[name="viewport"]').setAttribute('content', 
        'width=' + originalWidth + ', height=' + originalHeight + ', user-scalable=no');
    console.log('Size window restored')
    }


eel.expose(exit_frontend);
function exit_frontend() {
    console.log("Exit web");
    window.close();
}