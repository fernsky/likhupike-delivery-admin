/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: process.env.NEXT_PUBLIC_BASE_URL || 'https://digital.likhupikemun.gov.np',
  generateRobotsTxt: true,
  sitemapSize: 7000,
  exclude: ['/admin/*', '/api/*', '/server/*'],
  robotsTxtOptions: {
    additionalSitemaps: [
      `${process.env.NEXT_PUBLIC_BASE_URL || 'https://digital.likhupikemun.gov.np'}/sitemap-index.xml`,
    ],
    policies: [
      {
        userAgent: '*',
        allow: '/',
      },
    ],
  },
  // Add locale alternates to URLs
  alternateRefs: [
    {
      href: `${process.env.NEXT_PUBLIC_BASE_URL || 'https://digital.likhupikemun.gov.np'}/en`,
      hreflang: 'en',
    },
    {
      href: `${process.env.NEXT_PUBLIC_BASE_URL || 'https://digital.likhupikemun.gov.np'}/ne`,
      hreflang: 'ne',
    },
  ],
};