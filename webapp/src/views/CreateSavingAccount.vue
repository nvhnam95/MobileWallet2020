<template>
  <div>
    <p>Your Balance is {{balance}} SGD</p>
    <input type="text" name="amount" v-model="amount" placeholder="How much do you want to save?" />
    <p>Saving type:</p>
    <select v-model="saving_type">
      <option
        v-for="saving_type in saving_types"
        v-bind:key="saving_type"
        v-bind:value="saving_type"
      >{{ saving_type }}</option>
    </select>
    <br />
    <br />
    <button type="button" v-on:click="deposit()">Create</button>

    <p>
      <router-link :to="{ name: 'customer-info' }" class="nav-link" active-class="active">Back</router-link>
    </p>
  </div>
</template>

<script>
import { API_PATH } from "@/constant"

export default {
  name: "CreateSavingAccount",
  props: {
    msg: String
  },
  mounted() {
    this.axios
      .get(API_PATH + "customers/info")
      .then(response => {
        console.log(response);
        this.balance = response.data.balance;
        this.username = response.data.username;
      })
      .catch(response => {
        console.log(response);
        localStorage.removeItem("auth-token");
        this.$router.push({ name: "login" });
      });
  },
  data() {
    return {
      balance: 0,
      amount: 0,
      saving_type: '',
      saving_types: ["yearly", "quarterly", "monthly", "every_minute"]
    };
  },
  components: {},
  methods: {
    deposit() {
      if (this.amount == "") {
        alert("Please provide amount");
      } else {
        this.axios
          .post(API_PATH + "saving-accounts", {
            balance: this.amount,
            saving_type: this.saving_type
          })
          .then(response => {
            console.log(response);
            alert("Created, thank you!");
            this.$router.push({ name: "customer-info" });
          })
          .catch(response => {
            console.log(response);
            alert("There are an error happened, please try again later");
          });
      }
    }
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
