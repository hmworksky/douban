<template>
  <div>
    <tome-header></tome-header>
    <home-swiper></home-swiper>
    <div>test</div>
  </div>

</template>

<script>
import TomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
export default {
  name: 'Home',
  components: {
    TomeHeader,
    HomeSwiper
  }
}
</script>

<style scoped>

</style>
