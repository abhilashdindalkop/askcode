/** create a module for your app **/
var App = angular.module('LoginApp', ['ui.router','ngCookies']);

/** App configuration **/
App.config(['$stateProvider', '$urlRouterProvider',
    function ($stateProvider, $urlRouterProvider) {

        $.support.cors = true;

        /** configure routes **/
        $urlRouterProvider.otherwise('/sign-in');

        $stateProvider.state('signIn', {
                url: '/sign-in',
                templateUrl: 'partials/signin.html',
                controller: 'SignInCtrl'
            })
            .state('signUp', {
                url: '/sign-up',
                templateUrl: 'partials/signup.html',
                controller: 'AddUserCtrl'
            })
            .state('Question', {
                url: '/my-questions',
                templateUrl: 'partials/myquestions.html',
                controller: 'myQuestionCtrl'
            })
            .state('Questiondetail', {
                url: '/questionDetail?question',
                templateUrl: 'partials/questionDetail.html',
                controller: 'QuestionDetailCtrl'
            })
            .state('searchText', {
                url: '/search',
                templateUrl: 'partials/search.html',
                controller: 'searchTextCtrl'
            })
            .state('searchDisplay', {
                url: '/search-display',
                templateUrl: 'partials/search.html',
                controller: 'searchTextCtrl'
            })
}]);


/** Manage run state **/
App.run(['$rootScope', '$urlRouter', '$state',
    function ($rootScope, $urlRouter, $state) {

}]);