from django.shortcuts import render

def portfolio(request):
    profile = {
        'name': 'Sebastian Hitz',
        'title': 'Web Developer',
        'about': 'Estudié Filosofía en la Universidad Nacional de La Plata. Partidario de la corriente analítica y detractor de la continental. Me gusta el Manga y el Anime, leer ciencia ficción, ver películas de terror y escuchar Heavy metal. Hace unos años me interesé por la programación y empecé a estudiar Java, y luego también Python y Javascript. La idea de este blog es compartir tutoriales tan simples como sea posible sobre las cosas que voy aprendiendo. Los frameworks que me interesan al día de hoy son sobre todo Django y Spring, aunque también podrás encontrar algo de React y Angular.',
        'technologies': [
            {'name': 'Django', 'logo': 'https://camo.githubusercontent.com/6a80635322ebe0161d84f17479108a3293c2fb620fc3f95458f64c35d6798d18/68747470733a2f2f63646e2e69636f6e2d69636f6e732e636f6d2f69636f6e73322f323130372f504e472f3531322f66696c655f747970655f646a616e676f5f69636f6e5f3133303634352e706e67', 'alt': 'django-logo'},
            {'name': 'Spring', 'logo': 'https://user-images.githubusercontent.com/25181517/117201470-f6d56780-adec-11eb-8f7c-e70e376cfd07.png', 'alt': 'spring-logo'},
            {'name': 'React', 'logo': 'https://daily-dev-tips.com/ezoimgfmt/cdn.hashnode.com/res/hashnode/image/upload/v1647492266631/rH6yDfWyJ.png?ezimgfmt=rs:380x337/rscb2/ngcb2/notWebP', 'alt': 'react-logo'},
            {'name': 'Angular', 'logo': 'https://user-images.githubusercontent.com/25181517/183890595-779a7e64-3f43-4634-bad2-eceef4e80268.png', 'alt': 'angular-logo'},
            {'name': 'MySQL', 'logo': 'https://user-images.githubusercontent.com/25181517/183896128-ec99105a-ec1a-4d85-b08b-1aa1620b2046.png', 'alt': 'mysql-logo'},
            {'name': 'Bootstrap', 'logo': 'https://user-images.githubusercontent.com/25181517/183898054-b3d693d4-dafb-4808-a509-bab54cf5de34.png', 'alt': 'bootstrap-logo'},
        ],
        'projects': [
            {'name': 'Wallet Wizzard', 'img': 'https://media.licdn.com/dms/image/D4D2DAQFRpNHA5QTQDQ/profile-treasury-image-shrink_800_800/0/1690730494173?e=1698433200&v=beta&t=_oFMp1i8ZeDFBQtevk6cbDLyfbpHbW7J6-F0ULTkGQo', 'alt': 'Captura del proyecto Wallet Wizzard', 'link': 'https://hitzseb-wallet-wizard.web.app/', 'description': 'Aplicación web para llevar cuentas de ganancias y gastos. Hecho con Spring y Angular. Se trata de una versión demo, con una base de datos H2 y alojada en render, por lo cual la información guardada se elimina a los pocos minutos de usar la aplicación.'}
            ],
    }
    return render(request, 'portfolio.html', {'profile': profile})

def contact(request):
    return render(request, 'contact.html', {'email': 'hitzseb@gmail.com'})
