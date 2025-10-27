import type { NextConfig } from "next";

const nextConfig: NextConfig = {
    output: "export",
    trailingSlash: true,
    distDir: "static",
};

export default nextConfig;
