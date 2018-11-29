const path = require('path')
const PrerenderSPAPlugin = require('prerender-spa-plugin')

module.exports = {
  configureWebpack: () => {
    if (process.env.NODE_ENV !== 'production') return;
    return {
      plugins: [
        new PrerenderSPAPlugin(
          // Absolute path to compiled SPA
          path.resolve(__dirname, 'dist'),
          // List of routes to prerender
          ['/'],
          // options
          {}
        ),
      ]
    }
  },
  chainWebpack: config => {
    //html loader
    config.module
      .rule('html')
      .test(/\.(html)$/)
      .use(
        {
          options: {
            // attrs: [':data-src']
          }
        }
      )
      .loader('html-loader')
      .end()
  }
}
