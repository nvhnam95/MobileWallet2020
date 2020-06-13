<template>
  <div>
    <p>Your Balance is {{balance}} SGD</p>
    <input type="text" name="amount" v-model="amount" placeholder="Amount" />
    <button type="button" v-on:click="deposit()">Deposit</button>

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
 data() {
    return {
      balance: 0,
      amount: 0
    };
  },
  components: {
  },
    methods: {
    deposit() {
      if (this.amount == "") {
        alert("Please provide amount");
      } else {
        this.axios
          .post(API_PATH + "customers/deposit", {
            amount: this.amount,
          })
          .then(response => {
            console.log(response);
            alert("Deposit done");
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
