<template>
  <div>
    <h2>Login</h2>
    <input type="text" name="username" v-model="input.username" placeholder="Username" />
    <input type="password" name="password" v-model="input.password" placeholder="Password" />
    <button type="button" v-on:click="nam_test()">Login</button>
  </div>
</template>

<script>
import { API_PATH } from "@/constant"

export default {
  name: "Login",
  props: {
    msg: String
  },
  data() {
    return {
      input: {
        username: ""
      }
    };
  },
  mounted() {
    
  },
  methods: {
    nam_test() {
      if (this.input.username == "" || this.input.password == "") {
        alert("Please provide Username and Password");
      } else {
        this.axios
          .post(API_PATH + "auth-tokens", {
            username: this.input.username,
            password: this.input.password
          })
          .then(response => {
            console.log(response);
            this.$emit("authenticated", true);
            localStorage.setItem('auth-token', response.data.token);
            var auth_token = localStorage.getItem("auth-token");
            this.axios.defaults.headers.common['Authorization'] = "Token " + auth_token
            this.$router.push({name: "customer-info"});
          })
          .catch(response => {
            console.log(response);
            alert("Cannot login with your credentials, please try again.");
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
</style>
