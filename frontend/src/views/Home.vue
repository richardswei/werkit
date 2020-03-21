<template>
  <div>
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
