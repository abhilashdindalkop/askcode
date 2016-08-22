/** controller for add User view **/

App.controller('SignInCtrl',['$scope','$state','UserServc',function($scope, $state, UserServc){
    $scope.myuser = {
    };
    
    $scope.authLogin = function(){
        UserServc.authLogin(angular.copy($scope.myuser)).then(function(data){
            $state.go('Question');
        },function(data){
             if(data.status==400){
                var obj = JSON.parse(data.responseText);
                obj = JSON.parse(obj);
                $scope.error_text = obj.error;
                
            }
        });
    }
    
}]);


App.controller('AddUserCtrl',['$scope','$state','UserServc',function($scope, $state ,UserServc){
    $scope.newUser = {
    };
    
    $scope.addUser = function(){

        UserServc.addUser(angular.copy($scope.newUser)).then(function(){ 
            $state.go('Question');
        },function(data){

        });

    }
    
}]);


App.controller('myQuestionCtrl',['$scope','$state', 'UserServc',function($scope, $state , UserServc){
    $scope.newQuestion = {};

    $scope.questionList = [];     

    $scope.tagList = [];

    UserServc.getQuestions().then(function(data){
             $scope.questionList = data.questions;
        },function(data){

        });


    $scope.addQuestion = function(){
            
            //Adding tags to this NewQuestion
            $scope.newQuestion.tagList = angular.copy($scope.tagList)
            
        UserServc.addQuestion(angular.copy($scope.newQuestion)).then(function(data){
            $scope.questionList.push(data.question);

            $scope.tagList = [];
            $scope.newQuestion = {};
        },function(data){

        });

    }

    $scope.addTag = function(){

        $scope.tagList.push({ 'name': $scope.newtag });

    }


    $scope.questionDetail =function(que){
        var que = angular.toJson(que);
        $state.go('Questiondetail',{'question' : que})
    }


}]);


App.controller('QuestionDetailCtrl',['$scope','$state', 'UserServc',function($scope, $state , UserServc){
    
    var question = angular.fromJson($state.params.question);

    $scope.answerList = [];
    $scope.newAnswer = {};

    $scope.question = question;

    UserServc.getAnswers(question.id).then(function(data){
             $scope.answerList = data;
        },function(data){

        });

    $scope.addAnswer = function(){
             $scope.newAnswer.question_id = question.id;

        UserServc.addAnswer(angular.copy($scope.newAnswer)).then(function(data){
            $scope.answerList.push(data)

            $scope.newAnswer = {}
        },function(data){

        });

    }

    $scope.give_ansVote = function(vote,ans){
            ans.vote = vote;
        UserServc.give_ansVote(ans).then(function(data){
            console.log(data);
        ans.votes=ans.votes?ans.votes:0;        
        ans.votes += vote;

        },function(data){

        });

    }
    


}]);


App.controller('searchTextCtrl',['$scope','$state', 'UserServc',function($scope, $state , UserServc){

    $scope.questionList = [];

    $scope.searchText = function(){
        UserServc.searchText($scope.searchtext).then(function(data){
             $scope.questionList = data;
             // $state.go('searchDisplay');
        },function(data){

        });

    }

    $scope.questionDetail =function(que){
        var que = angular.toJson(que);
        $state.go('Questiondetail',{'question' : que})
    }


}]);

