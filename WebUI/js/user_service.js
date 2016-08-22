/*** employee service ***/
App.factory('UserServc', ['$q','$cookies',
    function ($q, $cookies) {

        var sessionid = $cookies.get('stack_sessionid')     

        function addUser(data) {
            return $q(function(resolve, reject){

             $.ajax({
                   type: 'POST',
                   url: 'http://127.0.0.1:8000/api/users/',
                   data: JSON.stringify(data),
                   dataType: "json",
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                      var obj = JSON.parse(data);
                      sessionid = obj.sessionid;
                      console.log(sessionid)
                      $cookies.put('stack_sessionid', obj.sessionid);
                      resolve(data);
                   },
                   error: reject
               });

            });
        }

        function authLogin(data) {
            
            return $q(function(resolve, reject){

             $.ajax({
                   type: 'POST',
                   url: 'http://127.0.0.1:8000/api/signin/',
                   data: JSON.stringify(data),
                   dataType: "json",
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                      var obj = JSON.parse(data);
                      sessionid = obj.sessionid;
                      $cookies.put('stack_sessionid', obj.sessionid);
                      resolve(data);
                   },
                   error: reject
               });

            });
        }

        function getQuestions() {
            return $q(function(resolve, reject){

             $.ajax({
                   type: 'GET',
                   url: 'http://127.0.0.1:8000/question/questions/',
                   headers: {
                      'token': sessionid
                   },
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                    var obj = JSON.parse(data);
                       resolve(obj);
                   },
                   error: reject
               });

            });
        }

        function addQuestion(data) {
            return $q(function(resolve, reject){

             $.ajax({
                   type: 'POST',
                   url: 'http://127.0.0.1:8000/question/questions/',
                   headers: {
                      'token': sessionid
                   },
                   data: JSON.stringify(data),
                   dataType: "json",
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                    var obj = JSON.parse(data);
                       resolve(obj);
                   },
                   error: reject
               });

            });
        }

        function getAnswers(qid) {                   
            return $q(function(resolve, reject){

             $.ajax({
                   type: 'GET',
                   url: 'http://127.0.0.1:8000/question/answers/'+qid,
                   headers: {
                      'token': sessionid
                   },
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                  
                       resolve(data);
                   },
                   error: reject
               });

            });
        }

        function addAnswer(data) {
            return $q(function(resolve, reject){

             $.ajax({
                   type: 'POST',
                   url: 'http://127.0.0.1:8000/question/answers/',
                   headers: {
                      'token': sessionid
                   },
                   data: JSON.stringify(data),
                   dataType: "json",
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                       resolve(data);
                   },
                   error: reject
               });

            });
        }

      function searchText(data) {

        return $q(function(resolve, reject){

             $.ajax({
                   type: 'POST',
                   url: 'http://127.0.0.1:8000/question/search/',
                   data: JSON.stringify(data),
                   dataType: "json",
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                       resolve(data);
                   },
                   error: reject
               });

            });
        }

        

      function give_ansVote(data) {
            return $q(function(resolve, reject){

             $.ajax({
                   type: 'POST',
                   url: 'http://127.0.0.1:8000/question/answervote/',
                   headers: {
                      'token': sessionid
                   },
                   data: JSON.stringify(data),
                   dataType: "json",
                   contentType: "application/json",
                   crossDomain : true,
                   success: function(data) {
                    var obj = JSON.parse(data);
                       resolve(obj);
                   },
                   error: reject
               });

            });
        }

        return {
            addUser: addUser,
            authLogin: authLogin,
            addQuestion: addQuestion,
            getQuestions: getQuestions,
            getAnswers:getAnswers,
            addAnswer:addAnswer,
            searchText:searchText,
            give_ansVote:give_ansVote,
        }

}]);