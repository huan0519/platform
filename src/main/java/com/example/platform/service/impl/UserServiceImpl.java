package com.example.platform.service.impl;

import com.example.platform.entity.User;
import com.example.platform.repository.UserRepository;
import com.example.platform.service.UserService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

@Service
public class UserServiceImpl implements UserService {
    @Resource
    private UserRepository userRepository;
    @Override
    public String login(User user) {
        User one= userRepository.login(user);
        if(one==null){
            return "用户不存在，请先登录";
        }else {
            return "登录成功！";
        }
    }
    @Override
    public String register(User user) {
        User one = userRepository.login(user);
        if(one==null){
            int count = userRepository.register(user);
            if(count>0){
                return "注册成功！";
            }else {
                return "系统出现问题，注册失败";
            }
        }else {
            return "用户已存在，请登录";
        }
    }
}
