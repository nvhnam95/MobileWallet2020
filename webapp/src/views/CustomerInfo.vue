<template>
  <div>
    <div class="account-info">
      <h1>Customer Info</h1>
      <p>Hello {{username}}</p>
      <p>Your balance is <b>{{balance}}</b> SGD</p>
      <p>You have {{number_of_saving_account}} saving account(s), with {{total_interest}} SGD of interest until now.</p>
        <router-link :to="{ name: 'create-saving-account' }" class="nav-link" active-class="active">Create a new one?</router-link>
        <router-link :to="{ name: 'delete-saving-account' }" class="nav-link" active-class="active">Delete some</router-link>
    </div>
    <div>
      <p>
        <router-link
          :to="{ name: 'transfer-money' }"
          class="nav-link"
          active-class="active"
        >Tranfer money</router-link>
      </p>
      <p>
        <router-link :to="{ name: 'deposit' }" class="nav-link" active-class="active">Deposit</router-link>
      </p>
    </div>
  <br><br>
    <div class="functions">
      <h1>
        Transaction history
      </h1>
      <TransactionTable></TransactionTable>
    </div>
  </div>
</template>

<script>
import { API_PATH } from "@/constant"

import TransactionTable from "@/components/TransactionTable";
export default {
  name: "Register",
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
      this.axios
      .get(API_PATH + "saving-accounts")
      .then(response => {
        this.number_of_saving_account = response.data.length
        for (var i=0; i<this.number_of_saving_account; i++){
          this.total_interest += response.data[i].interest;
        }
        
      })
      .catch(response => {
        console.log(response);
        this.$router.push({ name: "login" });
      });
  },
  data() {
    return {
      balance: 0,
      username: "",
      number_of_saving_account: 0,
      total_interest: 0
    };
  },
  components: {
    TransactionTable
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
