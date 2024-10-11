package com.example.platform.config;

import com.example.platform.config.Interceptor.JWTInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class InterceptorConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(getJwtInterceptor())
                .addPathPatterns("/**");// 拦截所有请求，通过判断token决定是否需要登录
                //.excludePathPatterns("/user/login","/user/register","/**/export","/**/import","/**/upload","/file/**");
    }

    @Bean
    public JWTInterceptor getJwtInterceptor() {
        return new JWTInterceptor();
    }
}
