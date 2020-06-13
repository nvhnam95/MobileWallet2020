<template>
  <div>
    <p>Your Balance is {{balance}} SGD</p>
    <input type="text" name="amount" v-model="amount" placeholder="Amount" />
    <p>To:</p>
    <select v-model="username">
      <option
        v-for="username in usernames"
        v-bind:key="username"
        v-bind:value="username"
      >{{ username }}</option>
    </select>
    <br />
    <br />
    <button type="button" v-on:click="transfer()">Transfer</button>
    <p>
      <router-link :to="{ name: 'customer-info' }" class="nav-link" active-class="active">Back</router-link>
    </p>
  </div>
</template>

<script>
import { API_PATH } from "@/constant"

export default {
  name: "TransferMoney",
  props: {
    msg: String
  },
  data() {
    return {
      balance: 0,
      amount: "",
      usernames: [],
      username: ""
    };
  },
  components: {},
  methods: {
    transfer() {
      if (this.amount == "") {
        alert("Please provide amount.");
      } else if (this.username == "") {
        alert("Please Choose a receiver.");
      } else {
        this.axios
          .post(API_PATH + "transactions", {
            amount: this.amount,
            receiver: this.username
          })
          .then(response => {
            console.log(response);
            alert("Transfer completed.");
            this.$router.push({ name: "customer-info" });
          })
          .catch(response => {
            console.log(response);
            alert("There are an error happened, please try again later");
          });
      }
    }
  },
  mounted() {
    this.axios
      .get(API_PATH + "customers/info")
      .then(response => {
        console.log(response);
        this.current_username = response.data.username;
      })
      .catch(response => {
        console.log(response);
        this.$router.push({ name: "login" });
      });
    this.axios
      .get(API_PATH + "customers")
      .then(response => {
        console.log(response);
        for (let i = 0; i < response.data.length; i++) {
          if (response.data[i].username != this.current_username)
            this.usernames.push(response.data[i].username);
        }
      })
      .catch(response => {
        console.log(response);
        
      });
  }
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
