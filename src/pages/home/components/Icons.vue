<template>
    <div class="icons">
      <swiper :options="swiperOption">
        <swiper-slide v-for="(page, index) of pages" :key="index">
            <div class="icon" v-for="item of page" :key="item.id">
              <div class="icon-image">
                <img class="icon-image-content" :src="item.imgUrl" />
              </div>
              <p class="icon-desc" v-text="item.desc"></p>
          </div>
        </swiper-slide>
      </swiper>
    </div>
</template>

<script>
export default {
  name: 'HomeIcons',
  props: {
    list: Array
  },
  data () {
    return {
      swiperOption: {
        AutoPlay: false
      }
    }
  },
  computed: {
    pages () {
      const pages = []
      this.list.forEach((item, index) => {
        const page = Math.floor(index / 8)
        if (!pages[page]) {
          pages[page] = []
        }
        pages[page].push(item)
      })
      return pages
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  @import '~styles/mixins.styl'
  .icons >>> .swiper-container
    height: 0
    padding-bottom : 50%
    margin-top: .2rem
  .icon
    height: 0
    position: relative
    float: left
    width: 25%
    padding-bottom : 25%
    .icon-desc
      position: absolute
      bottom: 0
      right : 0
      left: 0
      height: .44rem
      line-height : .44rem
      color: $darkTextColor
      text-align: center
      ellipsis()
    .icon-image
      position: absolute
      top: 0
      right : 0
      left: 0
      bottom: .44rem
      box-sizing : border-box
      .icon-image-content
        display: block
        height: 100%
        margin: 0 auto

</style>
