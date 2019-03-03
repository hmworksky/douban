<template>
    <div class="icons">
      <swiper >
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
  data () {
    return {
      iconList: [
        {
          id: '0001',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/95/f3dd6c383aeb3b02.png',
          desc: '景点门票'
        },
        {
          id: '0002',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1804/5a/13ceb38dcf262f02.png',
          desc: '一日游'
        },
        {
          id: '0003',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1804/ff/fdf170ee89594b02.png',
          desc: '上海必游'
        },
        {
          id: '0004',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/76/eb88861d78fb9902.png',
          desc: '动植物园'
        },
        {
          id: '0005',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/b6/37560ece9c62b502.png',
          desc: '城市观光'
        },
        {
          id: '0006',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/bd/9f7b9b2b60c1502.png',
          desc: '踏青赏花'
        },
        {
          id: '0007',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/fa/2548667cb6e902.png',
          desc: '东方明珠'
        },
        {
          id: '0008',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/47/c2b659e048b11602.png',
          desc: '野生动物园'
        },
        {
          id: '0009',
          imgUrl: 'http://img1.qunarzz.com/piao/fusion/1803/de/f26be47a6bf02a02.png',
          desc: '上海迪士尼'
        }
      ]
    }
  },
  computed: {
    pages () {
      const pages = []
      this.iconList.forEach((item, index) => {
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
