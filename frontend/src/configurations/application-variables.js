import * as ApplicationVariableDev from "configurations/application-variables.dev";

export const APPLICATION_URL = process.env.APPLICATION_URL || ApplicationVariableDev.APPLICATION_URL;
export const JWT_TOKEN_NAME = process.env.JWT_TOKEN_NAME || ApplicationVariableDev.JWT_TOKEN_NAME;