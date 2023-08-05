import express from "express";
import { fileURLToPath } from "url";
import { dirname, join } from "path";
import serveStatic from "serve-static";

const app = express();
const port = process.env.PORT || 3000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Serve static files from the "dist" directory
const distPath = join(__dirname, "dist");
app.use(serveStatic(distPath));

// Send the React app's index.html for all other routes
app.get("*", (req, res) => {
  res.sendFile(join(distPath, "index.html"));
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
