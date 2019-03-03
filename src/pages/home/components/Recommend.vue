<template>
    <div>
      <div class="title">热销推荐</div>
      <ul>
        <li class="item border-bottom" v-for="item of itemList" :key="item.id">
          <img class="item-image" :src="item.itemUrl"/>
          <div class="item-info">
            <p class="item-title" v-text="item.itemTitle"></p>
            <p class="item-desc" v-text="item.itemDesc"></p>
            <button class="item-button" v-text="item.itemButtonName"></button>
          </div>
        </li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'HomeRecommend',
  data () {
    return {
      itemList: [
        {
          id: '0001',
          itemUrl: 'http://img1.qunarzz.com/sight/p0/1812/b9/b9cc3ab2fbe4f0e7a3.img.jpg_250x250_5ff88af1.jpg',
          itemTitle: '大连海洋博物馆',
          itemDesc: '浪漫大连首站',
          itemButtonName: '查看详情'
        },
        {
          id: '0002',
          itemUrl: 'http://img1.qunarzz.com/sight/p0/1812/b9/b9cc3ab2fbe4f0e7a3.img.jpg_250x250_5ff88af1.jpg',
          itemTitle: '大连海洋博物馆',
          itemDesc: '浪漫大连首站',
          itemButtonName: '查看详情'
        },
        {
          id: '0003',
          itemUrl: 'http://img1.qunarzz.com/sight/p0/1812/b9/b9cc3ab2fbe4f0e7a3.img.jpg_250x250_5ff88af1.jpg',
          itemTitle: '大连海洋博物馆',
          itemDesc: '浪漫大连首站',
          itemButtonName: '查看详情'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/mixins.styl'
  .title
    line-height : .8rem
    background: #eee
    text-indent: .2rem
    margin-top: .2rem
  .item
    display : flex
    height: 1.9rem
    overflow: hidden
    .item-image
      width: 1.7rem
      height: 1.7rem
      padding: .1rem
    .item-info
      flex: 1
      padding: .1rem
      min-width: 0
      .item-title
        line-height : .54rem
        font-size: .32rem
        ellipsis()
      .item-desc
        line-height: .4rem
        color: #ccc
        ellipsis()
      .item-button
        margin-top: .16rem
        line-height: .44rem
        background : #ff9300
        padding: 0 .1rem
        border-radius: .06rem
</style>
