import localFont from "next/font/local";

// 本地字体
export const fontSans = localFont({
  src: [
    {
      path: './inter/woff2/Inter-Light.woff2',
      weight: '300',
      style: 'normal',
    },
    {
      path: './inter/woff2/Inter-LightItalic.woff2',
      weight: '300',
      style: 'italic',
    },
    {
      path: './inter/woff2/Inter-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './inter/woff2/Inter-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './inter/woff2/Inter-Medium.woff2',
      weight: '500',
      style: 'normal',
    },
    {
      path: './inter/woff2/Inter-MediumItalic.woff2',
      weight: '500',
      style: 'italic',
    },
    {
      path: './inter/woff2/Inter-SemiBold.woff2',
      weight: '600',
      style: 'normal',
    },
    {
      path: './inter/woff2/Inter-SemiBoldItalic.woff2',
      weight: '600',
      style: 'italic',
    },
    {
      path: './inter/woff2/Inter-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './inter/woff2/Inter-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
  variable: "--font-sans",
  display: "swap",
});

export const fontMono = localFont({
  src: [
    {
      path: './fira-code/woff2/FiraCode-Light.woff2',
      weight: '300',
      style: 'normal',
    },
    {
      path: './fira-code/woff2/FiraCode-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './fira-code/woff2/FiraCode-Medium.woff2',
      weight: '500',
      style: 'normal',
    },
    {
      path: './fira-code/woff2/FiraCode-SemiBold.woff2',
      weight: '600',
      style: 'normal',
    },
    {
      path: './fira-code/woff2/FiraCode-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
  ],
  variable: "--font-mono",
  display: "swap",
});

