package com.example.platform.utils;

import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;

import java.util.Date;

public class TokenUtils {

    private static final long EXPIRE_TIME = 24 * 60 * 60 * 1000;

    public static String getToken(String username,String sign) {
        Date date = new Date(System.currentTimeMillis() + EXPIRE_TIME);
        return JWT.create().withAudience(username) // 将 username 保存到 token 里面
                .withExpiresAt(date) //一天后token过期
                .sign(Algorithm.HMAC256(sign)); // 以 password 作为 token 的密钥
    }
}
