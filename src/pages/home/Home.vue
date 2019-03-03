<template>
  <div>
    <tome-header></tome-header>
    <home-swiper></home-swiper>
    <home-icons></home-icons>
  </div>

</template>

<script>
import TomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
import HomeIcons from './components/Icons'
export default {
  name: 'Home',
  components: {
    TomeHeader,
    HomeSwiper,
    HomeIcons
  }
}
</script>

<style scoped>

</style>
