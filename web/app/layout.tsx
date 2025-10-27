import "@/styles/globals.css";
import { Metadata, Viewport } from "next";
import clsx from "clsx";
import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem
} from '@heroui/navbar';
import { Providers } from "./providers";

import { siteConfig } from "@/config/site";
import { fontSans, fontMono } from "@/styles/fonts";
import { VoyahLogoIcon } from "@/components/icons";
import { ThemeSwitch } from "@/components/ThemeSwitch";

// 定义全局页面元数据（如标题、描述、图标），用于 SEO 和浏览器标签显示
export const metadata: Metadata = {
  title: {
    default: siteConfig.name,
    template: `%s - ${siteConfig.name}`,
  },
  description: siteConfig.description,
  icons: {
    icon: "/favicon.ico",
  },
};


// 配置页面 viewport 相关信息，自动适配浅色/深色主题的浏览器主题色
export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "white" },
    { media: "(prefers-color-scheme: dark)", color: "black" },
  ],
};

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {

  return (
    <html suppressHydrationWarning>
      <head />
      <body
        className={clsx(
          "min-h-screen text-foreground bg-background font-sans antialiased",
          fontSans.variable,
          fontMono.variable,
        )}
      >
        <Providers
          themeProps={{ attribute: "class", defaultTheme: "dark" }}
        >
          <div className="relative flex flex-col h-screen">
            <Navbar
              maxWidth="full"
              position="sticky"
            >
              <NavbarBrand>
                <VoyahLogoIcon size={32} />
                <h2 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">
                  VAgent
                </h2>
              </NavbarBrand>


              <NavbarContent justify="end">
                <NavbarItem>
                  <ThemeSwitch />
                </NavbarItem>
              </NavbarContent>
            </Navbar>
            <main className="flex-1 overflow-hidden">
              {children}
            </main>
          </div>
        </Providers>
      </body>
    </html>
  );
}
