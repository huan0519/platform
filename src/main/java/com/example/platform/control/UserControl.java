package com.example.platform.control;

import com.example.platform.entity.User;
import com.example.platform.service.UserService;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/user")
public class UserControl {
    @Resource
    private UserService userService;
    @PostMapping("/login")
    public String login(@RequestBody User user) {
        return userService.login(user);
    }
    @PostMapping("/register")
    public String register(@RequestBody User user) {
        return userService.register(user);
    }
}
