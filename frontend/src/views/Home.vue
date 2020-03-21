<template>
  <div class="home background">
    <HomeWelcome/>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeWelcome from '@/components/HomeWelcome.vue';

export default {
  name: 'Home',
  components: {
    HomeWelcome,
  },
};
</script>

<style>
.home.background {
  background: url(../assets/background.png) no-repeat center center fixed;
  background-size: cover;
  height: 100%;
  /*overflow: hidden;*/
}
</style>
