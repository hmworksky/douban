<template>
  <div class="wrapper">
    <swiper :options="swiperOption" v-if="showSwiper">
    <!-- slides -->
    <swiper-slide v-for="item in list" :key="item.id">
      <img class="swiper-image" :src="item.imgUrl" />
    </swiper-slide>
    <!--<swiper-slide>-->
      <!--<img class="swiper-image" src="http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20193/278a88f18f1523eec8c52f650522be68.jpg_750x200_bc365244.jpg" />-->
    <!--</swiper-slide>-->

    <!-- Optional controls -->
    <div class="swiper-pagination"  slot="pagination"></div>
  </swiper>
  </div>
</template>

<script>
export default {
  name: 'HomeSwiper',
  props: {
    list: Array
  },
  data () {
    return {
      swiperOption: {
        pagination: '.swiper-pagination', // 分页配置
        loop: true // 支持轮播
      }
    }
  },
  computed: {
    showSwiper () {
      return this.list.length
    }
  }
}
</script>

<style lang="stylus" scoped>
  // 通过3个箭头穿透样式，只要在当前页面中发现则修改该样式
  .wrapper >>> .swiper-pagination-bullet-active
      background: #ffffff
  .wrapper
    // 高度宽度比
    width: 100%
    height: 0
    padding-bottom: 31.25%
    overflow : hidden
    .swiper-image
      width: 100%

</style>
