import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      name: "home",
      path: "/",
      component: () => import("@/views/Home.vue")
    },
    {
      name: "login",
      path: "/login",
      component: () => import("@/views/Login.vue")
    },
    {
      name: "register",
      path: "/register",
      component: () => import("@/views/Register.vue")
    },    
    {
      name: "customer-info",
      path: "/customer-info",
      component: () => import("@/views/CustomerInfo.vue")
    },
    {
      name: "deposit",
      path: "/deposit",
      component: () => import("@/views/Deposit.vue")
    },
    {
      name: "transfer-money",
      path: "/transfer-money",
      component: () => import("@/views/TransferMoney.vue")
    },
    {
      name: "create-saving-account",
      path: "/create-saving-account",
      component: () => import("@/views/CreateSavingAccount.vue")
    },
    {
      name: "delete-saving-account",
      path: "/delete-saving-account",
      component: () => import("@/views/DeleteSavingAccount.vue")
    },
  ]
});
