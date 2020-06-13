<template>
  <v2-table :data="data">
    <v2-table-column label="Transaction ID" prop="id"></v2-table-column>
    <v2-table-column label="Sender" prop="sender"></v2-table-column>
    <v2-table-column label="Receiver" prop="receiver"></v2-table-column>  
    <v2-table-column label="Amount" prop="amount"></v2-table-column>  
    <v2-table-column label="Time" prop="created_time"></v2-table-column>  
  </v2-table>  
</template>

<script>
export default {
  data() {
    return {
      "data": []
    };
  },
  mounted() {
    this.axios
      .get("http://localhost/api/v1/transactions")
      .then(response => {
        console.log(response);
        this.data = response.data;
      })
      .catch(response => {
        console.log(response);
      });
  }
};
</script>
