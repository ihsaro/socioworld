import { APPLICATION_URL as DEV_APPLICATION_URL } from "configurations/application-variables.dev";

export const APPLICATION_URL = process.env.APPLICATION_URL || DEV_APPLICATION_URL;