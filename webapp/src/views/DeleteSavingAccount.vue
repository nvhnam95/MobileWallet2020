<template>
  <div>
    <p>Which one do you want to delete?</p>

    <select v-model="account">
      <option
        v-for="account in list_account"
        v-bind:key="account"
        v-bind:value="account"
      >{{ account }}</option>
    </select>
    <br/>
    <br/>

    <button type="button" v-on:click="delete_saving_account()">Delete</button>

      <p>
        <router-link
          :to="{ name: 'customer-info' }"
          class="nav-link"
          active-class="active"
        >Back</router-link>
      </p>

    </div>

</template>

<script>
import { API_PATH } from "@/constant"

export default {
  name: "Deposit",
  props: {
    msg: String
  },
   mounted() {
    this.axios
      .get(API_PATH + "saving-accounts")
      .then(response => {
        console.log(response);
        for (var i=0; i<response.data.length; i++){
        this.list_account.push(response.data[i].id + " - Interest: " + response.data[i].interest);
        }
      })
      .catch(response => {
        console.log(response);
        localStorage.removeItem("auth-token");
        this.$router.push({ name: "login" });
      });
  },
 data() {
    return {
      id: 0,
      list_account: [],
      account: ''
    };
  },
  components: {
  },
    methods: {
    delete_saving_account() {
      if (this.account == "") {
        alert("Please select one account");
      } else {
        this.id = this.account.split("-")[0];
        this.axios
          .deleteAPI_PATH + ("saving-accounts/" + this.id)
          .then(response => {
            console.log(response);
            alert("Deleted!");
            this.$router.push({name: "customer-info"});
          })
          .catch(response => {
            console.log(response);
            alert("There are an error happened, please try again later");
          });
      }
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
