 
//we have created an app for the ng-app mentioned in our page and included the ngRoute for routing configuration  
var myApp = angular.module("myApp", ['ngRoute']);  
//start configuring routes  
myApp.config(['$routeProvider', function($routeProvider)  
{  
    $routeProvider  
    //when the home page is requested then call the view "home.html" and at the same time dynamically assign the controller "homeCtrl" to the page  
    .when('/',  
    {  
        templateUrl: 'home.html'  
    })  
    //when the requested url is "/about" then call the view "about.html" and assign the controller "aboutCtrl" to it  
    .when('/about',  
    {  
        templateUrl: 'about.html'   
    })  
    //when the requested url is '/contact then call the view "contact.html" and assign the controller "contactCtrl" to it  
    .when('/contact',  
    {  
        templateUrl: 'contact.html' 
    })  
    .when('/faq',  
    {  
        templateUrl: 'faq.html' 
    })  
    .when('/register',  
    {  
        templateUrl: 'register.html' 
    })  
    //in case any other url is requested then direct the user to home page  
    .otherwise(  
    {  
        redirectTo: '/'  
    });  
}])