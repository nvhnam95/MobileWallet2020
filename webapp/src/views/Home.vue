<template>
  <div>
      <div>Hello, welcome to MobileWallet2020</div><br>
    <router-link :to="{ name: 'login' }" class="nav-link" active-class="active">Login</router-link>
    <br><router-link :to="{ name: 'register' }" class="nav-link" active-class="active">Register</router-link>

  </div>
</template>

<script>
export default {
  name: "Register",
  props: {
    msg: String
  },
  mounted() {
    var token = localStorage.getItem("auth-token");
    if (token){
      this.$router.push({name: "customer-info"});
    }
  },
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
