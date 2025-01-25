import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.scss";
import LayoutClient from "./layout.client";
import RootLayoutClient from "./layout.client";
// import { getServerSession } from "next-auth/next"
// import { options } from "./api/auth/[...nextauth]/route";
// import { Session } from "next-auth";

// const geistSans = localFont({
//   src: "./fonts/GeistVF.woff",
//   variable: "--font-geist-sans",
//   weight: "100 900",
// });
// const geistMono = localFont({
//   src: "./fonts/GeistMonoVF.woff",
//   variable: "--font-geist-mono",
//   weight: "100 900",
// });

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default async function RootLayout({
  children, 
}: Readonly<{
  children: React.ReactNode;
  // session: Session | null
}>) {
  // const session = await getServerSession(options)
  return (
    <html lang="en">
      <body>
        <RootLayoutClient>{children}</RootLayoutClient>
      </body>
    </html>
  );
}
