<template>
  <div>
    <h2>Register</h2>
    <input type="text" name="username" v-model="input.username" placeholder="Username" />
    <br><br><input type="password" name="password1" v-model="input.password1" placeholder="Password" />
    <br><br><input type="password" name="password2" v-model="input.password2" placeholder="Enter your password again" />

    <br><br><br><button type="button" v-on:click="register()">Register</button>
  </div>
</template>

<script>
import { API_PATH } from "@/constant"

export default {
  name: "Register",
  props: {
    msg: String
  },
  data() {
    return {
      input: {
        username: "",
        password1: "",
        password2: ""
      }
    };
  },
  methods: {
    register() {
      if (this.input.username == "" || this.input.password1 == "" || this.input.password2 == "") {
        alert("Please provide Username and Password");
      } else if (this.input.password1 != this.input.password2) {
        alert("Password doesnot match.");
      }
      else {
        this.axios
          .post(API_PATH + "customers", {
            username: this.input.username,
            password: this.input.password1
          })
          .then(response => {
            console.log(response);
            alert("Register successfully.");
            this.$router.push({name: "login"});
          })
          .catch(response => {
            console.log(response);
            if (response.response.data.password)
            alert(response.response.data.password);
            if (response.response.data.username)
            alert(response.response.data.username);

            this.input.username = "";
            this.input.password = "";
          });
      }
    }
  },
  components: {}
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
input {
	margin:10px auto;
	max-width: 400px;
	padding: 20px 12px 10px 20px;
	font: 13px "Lucida Sans Unicode", "Lucida Grande", sans-serif;
}
input li {
	padding: 0;
	display: block;
	list-style: none;
	margin: 10px 0 0 0;
}
input label{
	margin:0 0 3px 0;
	padding:0px;
	display:block;
	font-weight: bold;
}
.input input[type=text], 
.input input[type=date],
.input input[type=datetime],
.input input[type=number],
.input input[type=search],
.input input[type=time],
.input input[type=url],
.input input[type=email],
textarea, 
select{
	box-sizing: border-box;
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	border:1px solid #BEBEBE;
	padding: 7px;
	margin:0px;
	-webkit-transition: all 0.30s ease-in-out;
	-moz-transition: all 0.30s ease-in-out;
	-ms-transition: all 0.30s ease-in-out;
	-o-transition: all 0.30s ease-in-out;
	outline: none;	
}
.input input[type=text]:focus, 
.input input[type=date]:focus,
.input input[type=datetime]:focus,
.input input[type=number]:focus,
.input input[type=search]:focus,
.input input[type=time]:focus,
.input input[type=url]:focus,
.input input[type=email]:focus,
.input textarea:focus, 
.input select:focus{
	-moz-box-shadow: 0 0 8px #88D5E9;
	-webkit-box-shadow: 0 0 8px #88D5E9;
	box-shadow: 0 0 8px #88D5E9;
	border: 1px solid #88D5E9;
}
.input .field-divided{
	width: 49%;
}

.input .field-long{
	width: 100%;
}
.input .field-select{
	width: 100%;
}
.input .field-textarea{
	height: 100px;
}
.input input[type=submit], .input input[type=button]{
	background: #4B99AD;
	padding: 8px 15px 8px 15px;
	border: none;
	color: #fff;
}
.input input[type=submit]:hover, .input input[type=button]:hover{
	background: #4691A4;
	box-shadow:none;
	-moz-box-shadow:none;
	-webkit-box-shadow:none;
}
.input .required{
	color:red;
}
</style>