import express, {Router} from 'express';
import serverless from "serverless-http";
import userRoutes from "../../routes/userRoutes.js";

const api = express()

api.use("/api/",userRoutes);

export const handler = serverless(api);