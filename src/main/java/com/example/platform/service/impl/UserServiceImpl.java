package com.example.platform.service.impl;

import com.example.platform.common.constants;
import com.example.platform.common.result;
import com.example.platform.entity.User;
import com.example.platform.exception.ServiceException;
import com.example.platform.repository.UserRepository;
import com.example.platform.service.UserService;
import com.example.platform.utils.TokenUtils;
import org.springframework.boot.web.embedded.netty.NettyReactiveWebServerFactory;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

@Service
public class UserServiceImpl implements UserService {
    @Resource
    private UserRepository userRepository;
    @Override
    public User login(User user) {
        User one= userRepository.login(user);
        if(one==null){
            throw new ServiceException(constants.code_400,"用户不存在，请先注册");
        }else {
            String token = TokenUtils.getToken(one.getUsername(),one.getPassword());
            one.setToken(token);
            return one;
        }
    }
    @Override
    public User register(User user) {
        User one = userRepository.selectByUsername(user.getUsername());
        if(one==null){
            int count = userRepository.register(user);
            if(count>0){
                return user;
            }else {
                throw new ServiceException(constants.code_400,"系统出现问题，注册失败");
            }
        }else {
            throw new ServiceException(constants.code_400,"用户已存在，请登录");
        }
    }

    @Override
    public User selectByUsername(String username) {
        User one = userRepository.selectByUsername(username);
        if(one==null){
            throw new ServiceException(constants.code_400,"系统错误，用户信息不存在");
        }else {
            return one;
        }
    }
}
