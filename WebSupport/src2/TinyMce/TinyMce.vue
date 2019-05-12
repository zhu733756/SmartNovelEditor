<template>
  <div class="editor">
    <editor id="tinymceEditor" :init="tinymceInit" v-model="content" :key="tinymceFlag"></editor>

  </div>
</template>

<script>
  import tinymce from 'tinymce/tinymce'
  import 'tinymce/themes/silver/theme'
  import Editor from '@tinymce/tinymce-vue'
  import 'tinymce/plugins/textcolor'
  import 'tinymce/plugins/advlist'
  import 'tinymce/plugins/table'
  import 'tinymce/plugins/lists'
  import 'tinymce/plugins/paste'
  import 'tinymce/plugins/preview'
  import 'tinymce/plugins/fullscreen'
  import 'tinymce/plugins/save'
  import axios from 'axios'

  // Initialize
  export default {
    name: 'tiny-mce',
    data() {
      return {
        tinymceFlag: 1,
        tinymceInit: {},
        html: ""
      }
    },
    computed: {
      params:
        function () {
          return this.$route.params
        },
      content: {
        get: function () {
          return this.$route.params.content
        },
        set: function () {

        }
      },
      saveParams: function () {
        const params = this.params;
        params.content = this.html;
        return params
      },
      isChanged: function () {
        return this.html != this.content
      }
    },
    components: {
      Editor
    },
    created() {
      const that = this;
      this.tinymceInit = {
        skin_url: `/static/tinymce/skins/ui/oxide`,
        // language_url: `/static/=tinymce/langs/zh_CN.js`,
        // language: 'zh_CN',
        indent_use_margin: true,
        indentation: 20,
        height: document.documentElement.clientHeight,
        browser_spellcheck: true, // 拼写检查
        branding: false, // 去水印
        elementpath: false,  //禁用编辑器底部的状态栏
        statusbar: true, // 隐藏编辑器底部的状态栏
        paste_data_images: true, // 允许粘贴图像
        menu: ['file', "edit", "view"],
        plugins: 'advlist table lists paste preview fullscreen',
        toolbar: [
          'fontselect fontsizeselect forecolor backcolor bold italic underline strikethrough',
          'alignleft aligncenter alignright alignjustify | quicklink h2 h3 preview fullscreen save'
        ],
        setup: (editor) => {
          // 初次化编辑器
          editor.on('init', () => {
            // 设置默认值
            editor.setContent('<p>' + this.content + '</p>');
            // 注册事件
            editor.on('input change undo redo', () => {
              // 获得编辑结果
              this.html = editor.getContent();
            });
          });
          editor.ui.registry.addButton('save', {
            icon: 'save',
            // 使用tinymce save图标插件
            tooltip: 'save',
            onAction: () => {
              console.log(this.isChanged);
              if (this.isChanged) {
                axios.get('/api/tinymce/store/', {params: this.saveParams}).then(
                  response => {
                    const data = response.data;
                    if (data.status == 200) {
                      alert("保存成功!")
                    }
                  }
                ).catch(err => {
                  alert("请求出错！")
                })
              }
            }
          });
        }
      }
    },
    activated() {
      this.tinymceFlag++
    },
    destroyed() {
      tinymce.get(this.id).destroyed()
    },
  }
</script>

<style>
  .el-main {
    padding: 0px;
  }
</style>
